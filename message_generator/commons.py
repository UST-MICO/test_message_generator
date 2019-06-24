

def prepare_logging(log_file_path, log_format, log_level):
    import logging
    logging.basicConfig(
        level=logging.getLevelName(log_level),
        format=log_format,
        handlers=[
             logging.FileHandler(filename=log_file_path),
             logging.StreamHandler()]
    )


def get_env_variable_str(d):
    return "\n ".join(["{}: {}".format(k, v) for k, v in d.items()
            if k.startswith('KAFKA_') or k.startswith('MESSAGE_' or k.startswith) or k.startswith('LOG_')])