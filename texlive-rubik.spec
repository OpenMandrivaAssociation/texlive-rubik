# revision 32919
# category Package
# catalog-ctan /macros/latex/contrib/rubik
# catalog-date 2014-02-07 11:34:07 +0100
# catalog-license lppl1.3
# catalog-version 2.0
Name:		texlive-rubik
Version:	2.0
Release:	3
Summary:	Document Rubik cube configurations and rotation sequences
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rubik
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rubik.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rubik.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rubik.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-rubik.bin = %{EVRD}

%description
The bundle provides two packages: rubikcube provides commands
for typesetting Rubik cubes and their transformations; and
rubikrotation which can process a sequence of Rubik rotation
moves, with the help of a Perl package executed via \write18
(shell escape) commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/rubikrotation
%{_texmfdistdir}/scripts/rubik/rubikrotation.pl
%{_texmfdistdir}/tex/latex/rubik/rubikcube.sty
%{_texmfdistdir}/tex/latex/rubik/rubikrotation.sty
%doc %{_texmfdistdir}/doc/latex/rubik/README
%doc %{_texmfdistdir}/doc/latex/rubik/Rubik_doc_figA.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/Rubik_doc_figB.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/Rubik_doc_figC.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/Rubik_doc_figD.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/Rubik_doc_figE.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/Rubikrot_doc_figA.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/Rubikrot_doc_figB.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/example-cube.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/example-cube.tex
%doc %{_texmfdistdir}/doc/latex/rubik/example-rot1.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/example-rot1.sh
%doc %{_texmfdistdir}/doc/latex/rubik/example-rot1.tex
%doc %{_texmfdistdir}/doc/latex/rubik/example-rot2.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/example-rot2.sh
%doc %{_texmfdistdir}/doc/latex/rubik/example-rot2.tex
%doc %{_texmfdistdir}/doc/latex/rubik/rubikcube.pdf
%doc %{_texmfdistdir}/doc/latex/rubik/rubikrotation.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rubik/example-rot1.bat
%doc %{_texmfdistdir}/source/latex/rubik/example-rot2.bat
%doc %{_texmfdistdir}/source/latex/rubik/rubikcube.dtx
%doc %{_texmfdistdir}/source/latex/rubik/rubikcube.ins
%doc %{_texmfdistdir}/source/latex/rubik/rubikrotation.dtx
%doc %{_texmfdistdir}/source/latex/rubik/rubikrotation.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/rubik/rubikrotation.pl rubikrotation
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
