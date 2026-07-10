%global tl_name avantgar
%global tl_revision 77161

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	URW Base 35 font pack for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/urw/base35
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/avantgar.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus
Mono L (substituting for Adobe's Courier); Nimbus Roman No9 L
(substituting for Adobe's Times); Nimbus Sans L (substituting for
Adobe's Helvetica); Standard Symbols L (substituting for Adobe's
Symbol); URW Bookman; URW Chancery L Medium Italic (substituting for
Adobe's Zapf Chancery); URW Gothic L Book (substituting for Adobe's
Avant Garde); and URW Palladio L (substituting for Adobe's Palatino).

%prep
%setup -q -c
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/dvips
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/dvips/avantgar
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/fonts/afm/adobe
%dir %{_datadir}/texmf-dist/fonts/afm/urw
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/adobe
%dir %{_datadir}/texmf-dist/fonts/tfm/urw35vf
%dir %{_datadir}/texmf-dist/fonts/type1/urw
%dir %{_datadir}/texmf-dist/fonts/vf/adobe
%dir %{_datadir}/texmf-dist/fonts/vf/urw35vf
%dir %{_datadir}/texmf-dist/tex/latex/avantgar
%dir %{_datadir}/texmf-dist/fonts/afm/adobe/avantgar
%dir %{_datadir}/texmf-dist/fonts/afm/urw/avantgar
%dir %{_datadir}/texmf-dist/fonts/map/dvips/avantgar
%dir %{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar
%dir %{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar
%dir %{_datadir}/texmf-dist/fonts/type1/urw/avantgar
%dir %{_datadir}/texmf-dist/fonts/vf/adobe/avantgar
%dir %{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar
%{_datadir}/texmf-dist/dvips/avantgar/config.uag
%{_datadir}/texmf-dist/fonts/afm/adobe/avantgar/pagd8a.afm
%{_datadir}/texmf-dist/fonts/afm/adobe/avantgar/pagdo8a.afm
%{_datadir}/texmf-dist/fonts/afm/adobe/avantgar/pagk8a.afm
%{_datadir}/texmf-dist/fonts/afm/adobe/avantgar/pagko8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/avantgar/uagb8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/avantgar/uagbi8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/avantgar/uagd8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/avantgar/uagdo8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/avantgar/uagk8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/avantgar/uagko8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/avantgar/uagr8a.afm
%{_datadir}/texmf-dist/fonts/afm/urw/avantgar/uagri8a.afm
%{_datadir}/texmf-dist/fonts/map/dvips/avantgar/uag.map
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagd.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagd7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagd8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagd8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagd8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagdc.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagdc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagdc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagdo.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagdo7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagdo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagdo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagdo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagk.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagk7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagk8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagk8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagk8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagkc.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagkc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagkc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagko.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagko7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagko8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagko8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/adobe/avantgar/pagko8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagb7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagb8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagb8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagb8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagbc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagbc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagbi7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagbi8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagbi8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagbi8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagbo7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagbo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagbo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagbo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagd7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagd8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagd8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagd8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagdc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagdc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagdo7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagdo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagdo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagdo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagk7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagk8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagk8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagk8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagkc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagkc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagko7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagko8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagko8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagko8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagr7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagr8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagr8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagr8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagrc7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagrc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagri7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagri8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagri8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagri8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagro7t.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagro8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagro8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw35vf/avantgar/uagro8t.tfm
%{_datadir}/texmf-dist/fonts/type1/urw/avantgar/uagd8a.pfb
%{_datadir}/texmf-dist/fonts/type1/urw/avantgar/uagd8a.pfm
%{_datadir}/texmf-dist/fonts/type1/urw/avantgar/uagdo8a.pfb
%{_datadir}/texmf-dist/fonts/type1/urw/avantgar/uagdo8a.pfm
%{_datadir}/texmf-dist/fonts/type1/urw/avantgar/uagk8a.pfb
%{_datadir}/texmf-dist/fonts/type1/urw/avantgar/uagk8a.pfm
%{_datadir}/texmf-dist/fonts/type1/urw/avantgar/uagko8a.pfb
%{_datadir}/texmf-dist/fonts/type1/urw/avantgar/uagko8a.pfm
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagd.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagd7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagd8c.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagd8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagdc.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagdc7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagdc8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagdo.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagdo7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagdo8c.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagdo8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagk.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagk7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagk8c.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagk8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagkc.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagkc7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagkc8t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagko.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagko7t.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagko8c.vf
%{_datadir}/texmf-dist/fonts/vf/adobe/avantgar/pagko8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagb7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagb8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagb8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagbc7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagbc8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagbi7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagbi8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagbi8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagbo7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagbo8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagbo8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagd7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagd8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagd8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagdc7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagdc8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagdo7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagdo8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagdo8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagk7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagk8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagk8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagkc7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagkc8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagko7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagko8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagko8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagr7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagr8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagr8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagrc7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagrc8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagri7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagri8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagri8t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagro7t.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagro8c.vf
%{_datadir}/texmf-dist/fonts/vf/urw35vf/avantgar/uagro8t.vf
%{_datadir}/texmf-dist/tex/latex/avantgar/8ruag.fd
%{_datadir}/texmf-dist/tex/latex/avantgar/omluag.fd
%{_datadir}/texmf-dist/tex/latex/avantgar/omsuag.fd
%{_datadir}/texmf-dist/tex/latex/avantgar/ot1uag.fd
%{_datadir}/texmf-dist/tex/latex/avantgar/t1uag.fd
%{_datadir}/texmf-dist/tex/latex/avantgar/ts1uag.fd
