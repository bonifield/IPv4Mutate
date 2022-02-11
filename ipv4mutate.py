from random import randint

class IPv4Mutate:
	""" mutates IPv4 addresses provided in traditional dotted-decimal notation, ex. 192.168.1.1 """
	
	#============================================================================
	# initialize
	#============================================================================
	def __init__(self, iparg):
		""" initialize the IP argument _iparg and run all setters """
		self._iparg = iparg
		self.call_setters(self._iparg)

	#============================================================================
	# each octet as binary
	#============================================================================
	def get_mutate_binary(self):
		""" getter for binary output """
		return(self._mutate_binary)

	def set_mutate_binary(self, z):
		""" create a binary representation of the octets """
		b = ["{0:08b}".format(int(x)) for x in z.split(".")]
		bb = ".".join(b)
		self._mutate_binary = bb

	#============================================================================
	# each octet as dotted-hexadecimal
	#============================================================================
	def get_mutate_dotted_hex(self):
		""" getter for hex output """
		return(self._mutate_dotted_hex)

	def set_mutate_dotted_hex(self, z):
		""" create a hexadecimal representation of the octets """
		h = [hex(int(x)) for x in z.split(".")]
		hh = ".".join(h)
		self._mutate_dotted_hex = hh

	#============================================================================
	# each octet into a single hexadecimal string
	#============================================================================
	def get_mutate_hex(self):
		""" getter for single-string hex output """
		return(self._mutate_hex)

	def set_mutate_hex(self, z):
		""" create a single-string hexadecimal representation of the octets """
		h = z.split(".")
		s = ""
		for i in h:
			s += str(format(int(i), '02x'))
		self._mutate_hex = "0x"+s

	#============================================================================
	# each octet as octal
	#============================================================================
	def get_mutate_octal(self):
		""" getter for octal output """
		return(self._mutate_octal)

	def set_mutate_octal(self, z):
		""" create an octal representation of the octets """
		o = [oct(int(x)) for x in z.split(".")]
		oo = ".".join(o).replace("o","")
		self._mutate_octal = oo

	#============================================================================
	# each octet as octal padded with between 1 and 20 leading zeros
	#============================================================================
	def get_mutate_octal_padded(self):
		""" getter for octal output padded with zeros """
		return(self._mutate_octal_padded)

	def set_mutate_octal_padded(self, z):
		""" create an octal representation of the octets, padded with between 1 and 20 leading zeros """
		o = [oct(int(x)) for x in z.split(".")]
		r = []
		for i in o:
			r.append("0"*randint(1,21) + str(i))
		oo = ".".join(r).replace("o","")
		self._mutate_octal_padded = oo

	#============================================================================
	# IP in typical dotted-decimal but with padded zeros
	#============================================================================
	def get_mutate_zero_padded(self):
		""" getter for dotted-decimal padded-zero output """
		return(self._mutate_zero_padded)

	def set_mutate_zero_padded(self, z):
		""" left-pad zeros onto the octets if they are less than 3 characters long """
		p = [x.zfill(3) for x in z.split(".")]
		pp = ".".join(p)
		self._mutate_zero_padded = pp

	#============================================================================
	# IP to decimal
	#============================================================================
	def get_mutate_decimal(self):
		""" getter for decimal output """
		return(self._mutate_decimal)

	def set_mutate_decimal(self, z):
		""" convert each octet using powers of 256 then add the sums """
		ip = [int(x) for x in z.split(".")]
		i1 = ip[0]*(256**3)
		i2 = ip[1]*(256**2)
		i3 = ip[2]*(256**1)
		i4 = ip[3]*(256**0)
		ipout = i1+i2+i3+i4
		self._mutate_decimal = ipout

	#============================================================================
	# IP stripped of middle zeros if present
	#============================================================================
	def get_mutate_zero_stripped(self):
		""" getter for middle-zero-stripped output """
		return(self._mutate_zero_stripped)

	def set_mutate_zero_stripped(self, z):
		""" strip middle octets if they are zeros """
		s = z.split(".")
		o = []
		for i in s:
			if i != "0":
				o.append(i)
		ss = ".".join(o)
		self._mutate_zero_stripped = ss

	#============================================================================
	# URL-encoded IP string
	#============================================================================
	def get_mutate_urlencoded(self):
		""" getter for URL-encoded output """
		return(self._mutate_urlencoded)

	def set_mutate_urlencoded(self, z):
		""" create a URL-encoded representation of the IP, including dots """
		q = ["%{0:0>2}".format(format(ord(char), "x")) for char in z]
		qq = "".join(q)
		self._mutate_urlencoded = qq

	#============================================================================
	# all-in-one processing
	#============================================================================
	def call_setters(self, x):
		self.set_mutate_binary(x)
		self.set_mutate_dotted_hex(x)
		self.set_mutate_hex(x)
		self.set_mutate_octal(x)
		self.set_mutate_octal_padded(x)
		self.set_mutate_zero_padded(x)
		self.set_mutate_zero_stripped(x)
		self.set_mutate_urlencoded(x)
		self.set_mutate_decimal(x)

	#============================================================================
	# attributes
	#============================================================================
	mutate_binary = property(get_mutate_binary)
	mutate_dotted_hex = property(get_mutate_dotted_hex)
	mutate_hex = property(get_mutate_hex)
	mutate_octal = property(get_mutate_octal)
	mutate_octal_padded = property(get_mutate_octal_padded)
	mutate_zero_padded = property(get_mutate_zero_padded)
	mutate_zero_stripped = property(get_mutate_zero_stripped)
	mutate_urlencoded = property(get_mutate_urlencoded)
	mutate_decimal = property(get_mutate_decimal)

	#============================================================================
	def __repr__(self):
		""" returns the provided argument during initialization (_iparg) """
		return(f"{self._iparg}")