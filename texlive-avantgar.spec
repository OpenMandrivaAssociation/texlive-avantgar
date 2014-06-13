# revision 31835
# category Package
# catalog-ctan /fonts/urw/base35
# catalog-date 2012-06-06 22:57:48 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-avantgar
Version:	20120606
Release:	6
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/avantgar.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: - Century Schoolbook (substituting for
Adobe's New Century Schoolbook); - Dingbats (substituting for
Adobe's Zapf Dingbats); - Nimbus Mono L (substituting for
Abobe's Courier); - Nimbus Roman No9 L (substituting for
Adobe's Times); - Nimbus Sans L (substituting for Adobe's
Helvetica); - Standard Symbols L (substituting for Adobe's
Symbol); - URW Bookman; - URW Chancery L Medium Italic
(substituting for Adobe's Zapf Chancery); - URW Gothic L Book
(substituting for Adobe's Avant Garde); and - URW Palladio L
(substituting for Adobe's Palatino).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/avantgar/config.uag
%{_texmfdistdir}/fonts/afm/adobe/avantgar/pagd8a.afm
%{_texmfdistdir}/fonts/afm/adobe/avantgar/pagdo8a.afm
%{_texmfdistdir}/fonts/afm/adobe/avantgar/pagk8a.afm
%{_texmfdistdir}/fonts/afm/adobe/avantgar/pagko8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagb8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagbi8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagd8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagdo8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagk8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagko8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagr8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagri8a.afm
%{_texmfdistdir}/fonts/map/dvips/avantgar/uag.map
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagd.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagd7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagd8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagd8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagd8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagk.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagk7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagk8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagk8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagk8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagkc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagkc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagkc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagko.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagko7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagko8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagko8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagko8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagd7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagd8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagd8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagd8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagk7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagk8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagk8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagk8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagkc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagkc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagko7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagko8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagko8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagko8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagri7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagri8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagri8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagro8t.tfm
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagd8a.pfb
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagd8a.pfm
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagdo8a.pfb
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagdo8a.pfm
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagk8a.pfb
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagk8a.pfm
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagko8a.pfb
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagko8a.pfm
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagd.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagd7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagd8c.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagd8t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdc.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdo.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagk.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagk7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagk8c.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagk8t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagkc.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagkc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagkc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagko.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagko7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagko8c.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagko8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagd7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagd8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagd8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagdc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagdc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagdo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagdo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagdo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagk7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagk8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagk8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagkc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagkc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagko7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagko8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagko8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagri7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagri8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagro8t.vf
%{_texmfdistdir}/tex/latex/avantgar/8ruag.fd
%{_texmfdistdir}/tex/latex/avantgar/omluag.fd
%{_texmfdistdir}/tex/latex/avantgar/omsuag.fd
%{_texmfdistdir}/tex/latex/avantgar/ot1uag.fd
%{_texmfdistdir}/tex/latex/avantgar/t1uag.fd
%{_texmfdistdir}/tex/latex/avantgar/ts1uag.fd

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}
