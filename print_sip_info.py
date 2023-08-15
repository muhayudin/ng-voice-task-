#this file requires two function, first one is used to check headers for task b, second function to print conetent of headers

def parse_headers(file_content):
    lines = file_content.split('\n')

    blank_line_index = lines.index('')
    headers = {line.split(':', 1)[0].lower(): line.split(':', 1)[1].strip() for line in lines[1:blank_line_index]}

    return headers


def print_sip_info(file_content):
    lines = file_content.split('\n')

    request_line = lines[0].strip()
    blank_line_index = lines.index('')
    headers = {line.split(':', 1)[0]: line.split(':', 1)[1].strip() for line in lines[1:blank_line_index]}

    body = lines[-1]

    request_parts = request_line.split()
    method = request_parts[0]
    request_uri = request_parts[1]

    print("The given SIP message is a request with:")
    print("Request:")
    print(f"  - Request-URI: {request_uri}")
    print(f"  - Method: {method}")
    print("  - Headers:")
    for header, value in headers.items():
        print(f"    {header}: {value}")
    print(f"  - Body:\n{body}")
