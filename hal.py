from module import XMPPModule
from halutils import getSensibleName

class Hal(XMPPModule):
	def handleMessage(self, msg):
		if "open the pod bay doors" in str(msg['body']).lower():
			self.xmpp.reply(msg, "I'm sorry {}. I'm afraid I can't do that.".format(getSensibleName(msg)))
