def acquire_api_key(api_name, credentials):
    # Ghost sends POST to provider, handles 2FA or captcha via Varyn
    response = GhostBot.request_key(api_name, credentials)
    if response.success:
        save_key_to_env(api_name, response.key)
        wire_into_bot(api_name)
        log_event(f"API key for {api_name} acquired and wired.")