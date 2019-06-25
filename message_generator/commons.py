

def prepare_logging(log_file_path, log_format, log_level):
    """
    Sets up the logging with an appropriate configuration
    :param log_file_path: str, path to the log file
    :param log_format: str, format of the logging
    :param log_level: str, the log level used levels are INFO, DEBUG
    :return: -
    """
    import logging
    logging.basicConfig(
        level=logging.getLevelName(log_level),
        format=log_format,
        handlers=[
             logging.FileHandler(filename=log_file_path),
             logging.StreamHandler()]
    )


def get_env_variable_str(d: dict):
    """
    Creates a list of all the environment variables, that are relevant for the message generator.
    :param d: dict, usually the the environment variables of the OS (as provided by os.locals())
    :return: [str], of the format "<variable name>: <variable value>"
    """
    return "\n ".join(["{}: {}".format(k, v) for k, v in d.items()
            if k.startswith('KAFKA_') or k.startswith('MESSAGE_' or k.startswith) or k.startswith('LOG_')])