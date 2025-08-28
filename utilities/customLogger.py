import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(
            filename="C:\\Users\\Prajwal Paple\\Desktop\\ADA\\Astrom-QA\\Automation-Astrom\\My-Project\\Logs\\"+"automation.log",
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO
        )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
