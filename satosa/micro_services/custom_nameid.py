'''
Custom microservice that can parse the subject of an assertion, determine if it is in UPN format, and convert to SamAccountName format.
'''

import logging
from ..base import ResponseMicroService

import re
logger = logging.getLogger(__name__)

class ConvertUpnToSamAccountFormat(ResponseMicroService):
    """
    Customizes a NameID if the format matches userPrincipalName.
    """

    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.domainToUpper = config["domain_to_upper"]

    def process(self, context, data):
        subject_id = data.subject_id
        regex = r'^([^@]+)@(.*)'
        logger.debug("Parsing NameID: {}".format (data.subject_id))
        if subject_id == None : 
            logger.warn("NameID is empty and will be skipped.")
            return super().process(context, data)
        parts = re.match(regex, subject_id)
        
        if parts != None : 
            data.subject_id = '{}\{}'.format(str.upper(parts[2]) if self.domainToUpper else parts[2], parts[1])
            logger.info('Converted {} to {}'.format(subject_id, data.subject_id))
        else:
            logger.info('{} did not match userPrincipalName format and was skipped.'.format(subject_id))
        return super().process(context, data)

