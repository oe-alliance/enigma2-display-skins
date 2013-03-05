SUBDIRS = skins

metadir = $(datadir)/meta
meta_DATA = index-enigma2-display.xml
CLEANFILES = index-enigma2-display.xml

index-enigma2-display.xml: $(top_srcdir)/genmetaindex.py $(top_srcdir)/skins/*/*/meta/skin_*.xml
	$(AM_V_GEN)$(PYTHON) $^ > $@
