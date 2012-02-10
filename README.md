About
=====

miniconv is a minimal drop-in-substitute for iconv. You might want to use it where an iconv implementation isn't available and you're OK with the limited number of supported encodings.

The following encodings are fully supported:

	ASCII, UTF-8, ISO-8859-1 (ISO-Latin-1, UCS-1), UCS-2LE, UCS-2BE,
	UCS-2-INTERNAL, UTF-16LE, UTF-16BE, UTF-16-INTERNAL, UCS-4LE,
	UCS-4BE, UCS-4-INTERNAL, UTF-32LE, UTF-32BE, UTF-32-INTERNAL
	
The following encodings can be decoded, but not encoded:

	ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-5, ISO-8859-6,
	ISO-8859-7, ISO-8859-8, ISO-8859-9, ISO-8859-10, ISO-8859-11,
	ISO-8859-13, ISO-8859-14, ISO-8859-15, ISO-8859-16, WINDOWS-1250,
	WINDOWS-1251, WINDOWS-1252, WINDOWS-1253, WINDOWS-1254,
	WINDOWS-1255, WINDOWS-1256, WINDOWS-1257, WINDOWS-1258, WINDOWS-874,
	CP1250, CP1251, CP1252, CP1253, CP1254, CP1255, CP1256, CP1257, 
	CP1258, CP874.

The INTERNAL variants equate to BE (big-endian) or LE (little-endian) depending on the byte order of the host platform. You must specify INTERNAL, BE or LE for multibyte encodings - there's no facility for reading a BOM.

GNU libiconv style //IGNORE and //TRANSLIT can be appended to encoding  names (though at this time, both equate to //IGNORE). When present, invalid characters or characters which cannot be represented in the target encoding are simply discarded.

Configuration
-------------

Modify config.h to suit your needs. Usually, all you need to do is make sure `__BIG_ENDIAN__` is correctly defined for big endian platforms.
