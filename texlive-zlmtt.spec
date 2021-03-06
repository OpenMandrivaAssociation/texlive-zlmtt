# revision 32984
# category Package
# catalog-ctan /fonts/zlmtt
# catalog-date 2014-02-16 09:31:31 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-zlmtt
Version:	1.01
Release:	2
Summary:	Use Latin Modern Typewriter fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/zlmtt
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zlmtt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zlmtt.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows selection of Latin Modern Typewriter fonts
with scaling and access to all its features. The package
requires the mweights package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zlmtt/il2zlmtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/il2zlmvtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/l7xzlmtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/l7xzlmvtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/ly1zlmtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/ly1zlmvtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/ot1zlmtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/ot1zlmvtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/ot4zlmtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/ot4zlmvtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/qxzlmtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/qxzlmvtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/t1zlmtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/t1zlmvtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/t5zlmtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/t5zlmvtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/ts1zlmtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/ts1zlmvtt.fd
%{_texmfdistdir}/tex/latex/zlmtt/zlmtt.sty
%doc %{_texmfdistdir}/doc/fonts/zlmtt/README
%doc %{_texmfdistdir}/doc/fonts/zlmtt/zlmtt-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/zlmtt/zlmtt-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
