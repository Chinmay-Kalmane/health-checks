import socket

def main():
    check_network()

def check_network():
    """Returns true if it succeeds to resolve Google's URL, false otherwise."""
    try:
        socket.gethostbyname("www.google.com")
        return True
    except:
        return False
    
main()