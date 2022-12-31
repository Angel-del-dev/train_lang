def check_amount_params(args, max_args, fname):
    if len(args) > max_args:
        print(f"The {fname} function only allowes {max_args} parameter/s, {len(args)} given")
        return False
    return True