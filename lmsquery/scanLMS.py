#!/usr/bin/env ipython
#!/usr/bin/env python
# coding: utf-8


# In[6]:


#get_ipython().run_line_magic('alias', 'nbconvert nbconvert scanLMS.ipynb')




# In[10]:


#get_ipython().run_line_magic('nbconvert', '')




# In[3]:


import socket




# In[9]:


def scanLMS():
    '''
    Search local network for Logitech Media Servers
    Based on netdisco/lms.py by cxlwill - https://github.com/cxlwill
    returns list of dictionaries containing LMS servers ip and listen ports
    '''
    lmsIP  = '<broadcast>'
    lmsPort = 3483
    lmsMsg = b'eJSON\0'
    lmsTimeout = 2
<<<<<<< HEAD
    entries = []
=======
    
    entries = []
    
>>>>>>> 9bf8743447a2ac2c24e5fa4264b987943a122549
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    mySocket.settimeout(lmsTimeout)
    mySocket.bind(('', 0))
<<<<<<< HEAD
=======
    
>>>>>>> 9bf8743447a2ac2c24e5fa4264b987943a122549
    try:
        mySocket.sendto(lmsMsg, (lmsIP, lmsPort))
        while True: # loop until the timeout expires
            try:
                data, address = mySocket.recvfrom(1024) # read 1024 bytes from the socket
                if data and address:
                    port = None
                    if data.startswith(b'EJSON'):
                        position = data.find(b'N')
                        length = int(data[position+1:position+2].hex())
                        port = int(data[position+2:position+2+length])
<<<<<<< HEAD
                    entries.append({'host': address[0], 'port': port})

            except socket.timeout:
                break
    finally:
        mySocket.close()
=======
                    
                    entries.append({'host': address[0], 'port': port})
                        
                            

            except socket.timeout:
                break      
    finally:
        mySocket.close()
    
>>>>>>> 9bf8743447a2ac2c24e5fa4264b987943a122549
    return(entries)


