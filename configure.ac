AC_INIT([enigma2-display],1.0.0,[andrew.blackburn644@btinternet.com])
AM_INIT_AUTOMAKE([foreign])

m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

AM_PATH_PYTHON

AC_ARG_WITH(textlcd,
	AC_HELP_STRING([--with-textlcd], [use ascii based lcd, yes or no]),
	[[withtextlcd=$withval]],
	[[withtextlcd=no]]
)
if test x"$withtextlcd" != xno ; then
	AC_DEFINE(HAVE_TEXTLCD, 1,[Define when using an ascii based lcd device])
fi
AM_CONDITIONAL(HAVE_TEXTLCD, test x"$withtextlcd" != xno)

AC_ARG_WITH(colorlcd,
	AC_HELP_STRING([--with-colorlcd], [use 96x64 16bpp color display, yes or no]),
	[[withcolorlcd=$withval]],
	[[withcolorlcd=no]]
)
if test x"$withcolorlcd" != xno ; then
	AC_DEFINE(HAVE_COLORLCD, 1,[Define when using a 96x64 color display device])
fi
AM_CONDITIONAL(HAVE_COLORLCD, test x"$withcolorlcd" != xno)

AC_ARG_WITH(bwlcd96,
	AC_HELP_STRING([--with-bwlcd96], [use 96x64 1bpp black and white display, yes or no]),
	[[withbwlcd96=$withval]],
	[[withbwlcd96=no]]
)
if test x"$withbwlcd96" != xno ; then
	AC_DEFINE(HAVE_BWLCD96, 1,[Define when using a 96x64 black and white display device])
fi
AM_CONDITIONAL(HAVE_BWLCD96, test x"$withbwlcd96" != xno)

AC_ARG_WITH(bwlcd128,
	AC_HELP_STRING([--with-bwlcd128], [use 128x32 1bpp black and white display, yes or no]),
	[[withbwlcd128=$withval]],
	[[withbwlcd128=no]]
)
if test x"$withbwlcd128" != xno ; then
	AC_DEFINE(HAVE_BWLCD128, 1,[Define when using a 128x32 black and white display device])
fi
AM_CONDITIONAL(HAVE_BWLCD128, test x"$withbwlcd128" != xno)

AC_ARG_WITH(bwlcd140,
	AC_HELP_STRING([--with-bwlcd140], [use 140x32 1bpp black and white display, yes or no]),
	[[withbwlcd140=$withval]],
	[[withbwlcd140=no]]
)
if test x"$withbwlcd140" != xno ; then
	AC_DEFINE(HAVE_BWLCD140, 1,[Define when using a 140x32 black and white display device])
fi
AM_CONDITIONAL(HAVE_BWLCD140, test x"$withbwlcd140" != xno)

AC_ARG_WITH(colorlcd220,
	AC_HELP_STRING([--with-colorlcd220], [use 220x176 16bpp color display, yes or no]),
	[[withcolorlcd220=$withval]],
	[[withcolorlcd220=no]]
)
if test x"$withcolorlcd220" != xno ; then
	AC_DEFINE(HAVE_COLORLCD220, 1,[Define when using a 220x176 color display device])
fi
AM_CONDITIONAL(HAVE_COLORLCD220, test x"$withcolorlcd220" != xno)

AC_ARG_WITH(bwlcd255,
	AC_HELP_STRING([--with-bwlcd255], [use 255x64 1bpp black and white display, yes or no]),
	[[withbwlcd255=$withval]],
	[[withbwlcd255=no]]
)
if test x"$withbwlcd255" != xno ; then
	AC_DEFINE(HAVE_BWLCD255, 1,[Define when using a 255x64 black and white display device])
fi
AM_CONDITIONAL(HAVE_BWLCD255, test x"$withbwlcd255" != xno)

AC_ARG_WITH(colorlcd400,
	AC_HELP_STRING([--with-colorlcd400], [use 400x240 16bpp color display, yes or no]),
	[[withcolorlcd400=$withval]],
	[[withcolorlcd400=no]]
)
if test x"$withcolorlcd400" != xno ; then
	AC_DEFINE(HAVE_COLORLCD400, 1,[Define when using a 400x240 color display device])
fi
AM_CONDITIONAL(HAVE_COLORLCD400, test x"$withcolorlcd400" != xno)

AC_ARG_WITH(colorlcd480,
	AC_HELP_STRING([--with-colorlcd480], [use 400x320 16bpp color display, yes or no]),
	[[withcolorlcd480=$withval]],
	[[withcolorlcd480=no]]
)
if test x"$withcolorlcd480" != xno ; then
	AC_DEFINE(HAVE_COLORLCD480, 1,[Define when using a 480x320 color display device])
fi
AM_CONDITIONAL(HAVE_COLORLCD480, test x"$withcolorlcd480" != xno)

AC_ARG_WITH(colorlcd720,
	AC_HELP_STRING([--with-colorlcd720], [use 720x576 16bpp color display, yes or no]),
	[[withcolorlcd720=$withval]],
	[[withcolorlcd720=no]]
)
if test x"$withcolorlcd720" != xno ; then
	AC_DEFINE(HAVE_COLORLCD720, 1,[Define when using a 720x576 color display device])
fi
AM_CONDITIONAL(HAVE_COLORLCD720, test x"$withcolorlcd720" != xno)

AC_ARG_WITH(colorlcd800,
	AC_HELP_STRING([--with-colorlcd800], [use 800x480 16bpp color display, yes or no]),
	[[withcolorlcd800=$withval]],
	[[withcolorlcd800=no]]
)
if test x"$withcolorlcd800" != xno ; then
	AC_DEFINE(HAVE_COLORLCD800, 1,[Define when using a 800x480 color display device])
fi
AM_CONDITIONAL(HAVE_COLORLCD800, test x"$withcolorlcd800" != xno)


AC_OUTPUT([
Makefile
skins/Makefile
skins/display96/Makefile
skins/display96/LCDSkin_1/Makefile
skins/display96/LCDSkin_1/meta/Makefile
skins/display96/LCDSkin_2/Makefile
skins/display96/LCDSkin_2/meta/Makefile
skins/display128/Makefile
skins/display128/LCDSkin_1/Makefile
skins/display128/LCDSkin_1/meta/Makefile
skins/display128/LCDSkin_2/Makefile
skins/display128/LCDSkin_2/meta/Makefile
skins/display128/LCDSkin_3/Makefile
skins/display128/LCDSkin_3/meta/Makefile
skins/display128/LCDSkin_4/Makefile
skins/display128/LCDSkin_4/meta/Makefile
skins/display128/LCDSkin_5/Makefile
skins/display128/LCDSkin_5/meta/Makefile
skins/display140/Makefile
skins/display140/ubisIst_extlalarge/Makefile
skins/display140/ubisIst_extlalarge/meta/Makefile
skins/display140/ubisIst_normal/Makefile
skins/display140/ubisIst_normal/meta/Makefile
skins/display140/ubisIst_rotator/Makefile
skins/display140/ubisIst_rotator/meta/Makefile
skins/display140/LCDSkin_1/Makefile
skins/display140/LCDSkin_1/meta/Makefile
skins/display140/LCDSkin_2/Makefile
skins/display140/LCDSkin_2/meta/Makefile
skins/display220/Makefile
skins/display220/OE-A_LCDSkin_1/Makefile
skins/display220/OE-A_LCDSkin_1/meta/Makefile
skins/display220/OE-A_LCDSkin_2/Makefile
skins/display220/OE-A_LCDSkin_2/meta/Makefile
skins/display220/OE-A_LCDSkin_3/Makefile
skins/display220/OE-A_LCDSkin_3/meta/Makefile
skins/display220/OE-A_LCDSkin_4/Makefile
skins/display220/OE-A_LCDSkin_4/meta/Makefile
skins/display220/OE-A_LCDSkin_5/Makefile
skins/display220/OE-A_LCDSkin_5/meta/Makefile
skins/display220/OE-A_LCDSkin_6/Makefile
skins/display220/OE-A_LCDSkin_6/meta/Makefile
skins/display220/OE-A_LCDSkin_7/Makefile
skins/display220/OE-A_LCDSkin_7/meta/Makefile
skins/display220/OE-A_LCDSkin_8/Makefile
skins/display220/OE-A_LCDSkin_8/meta/Makefile
skins/display220/OE-A_LCDSkin_9/Makefile
skins/display220/OE-A_LCDSkin_9/meta/Makefile
skins/display255/Makefile
skins/display255/OE-A_LCDSkin_1/Makefile
skins/display255/OE-A_LCDSkin_1/meta/Makefile
skins/display255/OE-A_LCDSkin_2/Makefile
skins/display255/OE-A_LCDSkin_2/meta/Makefile
skins/display255/OE-A_LCDSkin_3/Makefile
skins/display255/OE-A_LCDSkin_3/meta/Makefile
skins/display255/OE-A_LCDSkin_4/Makefile
skins/display255/OE-A_LCDSkin_4/meta/Makefile
skins/display255/OE-A_LCDSkin_5/Makefile
skins/display255/OE-A_LCDSkin_5/meta/Makefile
skins/display255/OE-A_LCDSkin_6/Makefile
skins/display255/OE-A_LCDSkin_6/meta/Makefile
skins/display255/OE-A_LCDSkin_7/Makefile
skins/display255/OE-A_LCDSkin_7/meta/Makefile
skins/display255/OE-A_LCDSkin_8/Makefile
skins/display255/OE-A_LCDSkin_8/meta/Makefile
skins/display255/OE-A_LCDSkin_9/Makefile
skins/display255/OE-A_LCDSkin_9/meta/Makefile
skins/display255/OE-A_LCDSkin_10/Makefile
skins/display255/OE-A_LCDSkin_10/meta/Makefile
skins/display400/Makefile
skins/display400/OE-A_LCDSkin_1/Makefile
skins/display400/OE-A_LCDSkin_1/meta/Makefile
skins/display400/OE-A_LCDSkin_2/Makefile
skins/display400/OE-A_LCDSkin_2/meta/Makefile
skins/display400/OE-A_LCDSkin_3/Makefile
skins/display400/OE-A_LCDSkin_3/meta/Makefile
skins/display400/OE-A_LCDSkin_4/Makefile
skins/display400/OE-A_LCDSkin_4/meta/Makefile
skins/display400/OE-A_LCDSkin_5/Makefile
skins/display400/OE-A_LCDSkin_5/meta/Makefile
skins/display400/OE-A_LCDSkin_6/Makefile
skins/display400/OE-A_LCDSkin_6/meta/Makefile
skins/display400/OE-A_LCDSkin_7/Makefile
skins/display400/OE-A_LCDSkin_7/meta/Makefile
skins/display400/OE-A_LCDSkin_8/Makefile
skins/display400/OE-A_LCDSkin_8/meta/Makefile
skins/display400/OE-A_LCDSkin_9/Makefile
skins/display400/OE-A_LCDSkin_9/meta/Makefile
skins/display400/OE-A_LCDSkin_10/Makefile
skins/display400/OE-A_LCDSkin_10/meta/Makefile
skins/display400/OE-A_LCDSkin_11/Makefile
skins/display400/OE-A_LCDSkin_11/meta/Makefile
skins/display480/Makefile
skins/display480/OE-A_LCDSkin_1/Makefile
skins/display480/OE-A_LCDSkin_1/meta/Makefile
skins/display480/OE-A_LCDSkin_2/Makefile
skins/display480/OE-A_LCDSkin_2/meta/Makefile
skins/display480/OE-A_LCDSkin_3/Makefile
skins/display480/OE-A_LCDSkin_3/meta/Makefile
skins/display480/OE-A_LCDSkin_4/Makefile
skins/display480/OE-A_LCDSkin_4/meta/Makefile
skins/display480/OE-A_LCDSkin_5/Makefile
skins/display480/OE-A_LCDSkin_5/meta/Makefile
skins/display480/OE-A_LCDSkin_6/Makefile
skins/display480/OE-A_LCDSkin_6/meta/Makefile
skins/display480/OE-A_LCDSkin_7/Makefile
skins/display480/OE-A_LCDSkin_7/meta/Makefile
skins/display480/OE-A_LCDSkin_8/Makefile
skins/display480/OE-A_LCDSkin_8/meta/Makefile
skins/display720/Makefile
skins/display720/OE-A_LCDSkin_1/Makefile
skins/display720/OE-A_LCDSkin_1/meta/Makefile
skins/display720/OE-A_LCDSkin_2/Makefile
skins/display720/OE-A_LCDSkin_2/meta/Makefile
skins/display720/OE-A_LCDSkin_3/Makefile
skins/display720/OE-A_LCDSkin_3/meta/Makefile
skins/display720/OE-A_LCDSkin_4/Makefile
skins/display720/OE-A_LCDSkin_4/meta/Makefile
skins/display720/OE-A_LCDSkin_5/Makefile
skins/display720/OE-A_LCDSkin_5/meta/Makefile
skins/display720/OE-A_LCDSkin_6/Makefile
skins/display720/OE-A_LCDSkin_6/meta/Makefile
skins/display720/OE-A_LCDSkin_7/Makefile
skins/display720/OE-A_LCDSkin_7/meta/Makefile
skins/display800/Makefile
skins/display800/OE-A_LCDSkin_1/Makefile
skins/display800/OE-A_LCDSkin_1/meta/Makefile
skins/display800/OE-A_LCDSkin_2/Makefile
skins/display800/OE-A_LCDSkin_2/meta/Makefile
skins/display800/OE-A_LCDSkin_3/Makefile
skins/display800/OE-A_LCDSkin_3/meta/Makefile
skins/display800/OE-A_LCDSkin_4/Makefile
skins/display800/OE-A_LCDSkin_4/meta/Makefile
skins/display800/OE-A_LCDSkin_5/Makefile
skins/display800/OE-A_LCDSkin_5/meta/Makefile
skins/display800/OE-A_LCDSkin_6/Makefile
skins/display800/OE-A_LCDSkin_6/meta/Makefile
skins/display800/OE-A_LCDSkin_7/Makefile
skins/display800/OE-A_LCDSkin_7/meta/Makefile
skins/display800/OE-A_LCDSkin_8/Makefile
skins/display800/OE-A_LCDSkin_8/meta/Makefile
skins/display800/OE-A_LCDSkin_9/Makefile
skins/display800/OE-A_LCDSkin_9/meta/Makefile
skins/display800/OE-A_LCDSkin_10/Makefile
skins/display800/OE-A_LCDSkin_10/meta/Makefile
skins/display800/OE-A_LCDSkin_11/Makefile
skins/display800/OE-A_LCDSkin_11/meta/Makefile
skins/display800/OE-A_LCDSkin_12/Makefile
skins/display800/OE-A_LCDSkin_12/meta/Makefile
skins/display800/OE-A_LCDSkin_13/Makefile
skins/display800/OE-A_LCDSkin_13/meta/Makefile
skins/display800/OE-A_LCDSkin_14/Makefile
skins/display800/OE-A_LCDSkin_14/meta/Makefile
skins/display800/OE-A_LCDSkin_15/Makefile
skins/display800/OE-A_LCDSkin_15/meta/Makefile
skins/display800/OE-A_LCDSkin_16/Makefile
skins/display800/OE-A_LCDSkin_16/meta/Makefile
skins/display800/OE-A_LCDSkin_17/Makefile
skins/display800/OE-A_LCDSkin_17/meta/Makefile
skins/display800/OE-A_LCDSkin_18/Makefile
skins/display800/OE-A_LCDSkin_18/meta/Makefile
])
