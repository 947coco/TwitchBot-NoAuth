# -*- coding: utf-8 -*-
import socket

class Connection:
    def __init__(self, username):
        self.ChannelName = username
        self.NumberOfProcessedMsg = -2 # To ignore the 2 first welcome msg from the server
            
    def GetViewerName(self, raw_message):
        ViewerName = ""
        for letter in raw_message[1::]:
            if letter == "!": return ViewerName
            ViewerName += letter

    def GetChatMessage(self, raw_message):
        IndiceDebutMessage = raw_message.find(self.ChannelName) + len(self.ChannelName) + 2
        return raw_message[IndiceDebutMessage::]

    def ConnectionTwitchChat(self):
        """
        Connect to the twitch chat
        Use it only first time
        """
        nom = 'justinfan12345'  # Pseudo générique pour spectateurs anonymes
        token = 'oauth:1234567890abcdef'  # Token OAuth générique
        self.sock = socket.socket() # Création du socket
        self.sock.connect(('irc.chat.twitch.tv', 6667)) # Connection au server irc non-ssl de twitch

        # Authentification au serveur IRC
        self.sock.send(f"PASS {token}\r\n".encode('utf-8'))
        self.sock.send(f"NICK {nom}\r\n".encode('utf-8'))
        self.sock.send(f"JOIN #{self.ChannelName}\r\n".encode('utf-8'))

    def HandlePingVerification(self):
        """
        Handle the ping vérification cuz twitch check
        if you are still connected
        """
        resp = self.sock.recv(2048).decode('utf-8')
        if resp.startswith('PING'): 
            self.sock.send("PONG :tmi.twitch.tv\r\n".encode('utf-8'))

    def ProcessMessage(self):
        """
        Process the incoming message from twitch chat
        and return the name, message from viewer
        or 0, 0 if no message
        """
        resp = self.sock.recv(2048).decode('utf-8')
        if self.NumberOfProcessedMsg < 0: 
            self.NumberOfProcessedMsg += 1
            return 0, 0
        else :
            return self.GetViewerName(resp), self.GetChatMessage(resp)

    def FormatUserMessage(self, Username: str, Msg: str, format: str):
        """return the message according to FORMAT"""
        response = format
        response = response.replace("User", Username)
        response = response.replace("Message", Msg)
        return response

    


