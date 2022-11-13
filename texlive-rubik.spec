Name:		texlive-rubik
Version:	46791
Release:	1
Summary:	Document Rubik cube configurations and rotation sequences
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rubik
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rubik.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rubik.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rubik.source.r%{version}.tar.xz
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
%{_texmfdistdir}/scripts/rubik
%{_texmfdistdir}/tex/latex/rubik
%doc %{_texmfdistdir}/doc/latex/rubik
%doc %{_texmfdistdir}/doc/man/man1/*
#- source
%doc %{_texmfdistdir}/source/latex/rubik

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/rubik/rubikrotation.pl rubikrotation
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
