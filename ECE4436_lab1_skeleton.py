from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver = outlook
#Fill in start
mailserver = "smtp.gmail.com"
port = 587
#Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))


#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')



# Send HELO command and print server response. heloCommand = 'HELO Alice\r\n' clientSocket.send(heloCommand.encode())
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Start TLS for security
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv_starttls = clientSocket.recv(1024).decode()
print(recv_starttls)

# At this point, the client should upgrade the socket to TLS
import ssl

# Create an SSL context
context = ssl.create_default_context()
# Wrap the socket with SSL
secureSocket = context.wrap_socket(clientSocket, server_hostname='smtp.gmail.com')

# Authentication (fill in with valid email and password)
email_address = ' '
password = ' '

authCommand = f'AUTH LOGIN\r\n'
secureSocket.send(authCommand.encode())
recv_auth = secureSocket.recv(1024).decode()
print(recv_auth)

# Send the base64 encoded email address and password
import base64
secureSocket.send(base64.b64encode(email_address.encode()) + b'\r\n')
recv_auth_email = secureSocket.recv(1024).decode()
print(recv_auth_email)

secureSocket.send(base64.b64encode(password.encode()) + b'\r\n')
recv_auth_pass = secureSocket.recv(1024).decode()
print(recv_auth_pass)
# Send MAIL FROM command and print server response.
 
# Fill in start
mailFrom = f'MAIL FROM: <{email_address}>\r\n'
secureSocket.send(mailFrom.encode())
recv2 = secureSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
recipient = 'jakekot666@gmail.com'
rcptTo = f'RCPT TO: <{recipient}>\r\n'
secureSocket.send(rcptTo.encode())
recv3 = secureSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end




# Send DATA command and print server response.

# Fill in start
dataCommand = 'DATA\r\n'
secureSocket.send(dataCommand.encode())
recv4 = secureSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')
# Fill in end




# Send message data.

# Fill in start
secureSocket.send(msg.encode())



# Fill in end

# Message ends with a single period.

# Fill in start
secureSocket.send(endmsg.encode())
recv5 = secureSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.

# Fill in start
quitCommand = 'QUIT\r\n'
secureSocket.send(quitCommand.encode())
recv6 = secureSocket.recv(1024).decode()
print(recv6)
# Fill in end
secureSocket.close()
