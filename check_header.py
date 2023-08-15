#function to check headers and rexpective naming suggestion by Roy Osherove

from print_sip_info import parse_headers

def check_header(open_txt_file, target_header):
    headers = parse_headers(open_txt_file)
    lower_target_header = target_header.lower()  # Convert header to lowercase for case-insensitive comparison

    if lower_target_header in headers:
        header_content = headers[lower_target_header]
        return True, header_content
    else:
        return False, None
