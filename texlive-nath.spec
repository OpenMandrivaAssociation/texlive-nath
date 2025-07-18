Name:		texlive-nath
Version:	15878
Release:	2
Summary:	Natural mathematics notation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nath
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nath.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Nath is a LaTeX (both 2e and 2.09) style to separate
presentation and content in mathematical typography. The style
delivers a particular context-dependent presentation on the
basis of a rather coarse context-independent notation.
Highlighted features: depending on the context, the command
\frac produces either built-up or case or solidus fractions,
with parentheses added whenever required for preservation of
the mathematical meaning; delimiters adapt their size to the
material enclosed, rendering \left and \right almost obsolete.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nath
%doc %{_texmfdistdir}/doc/latex/nath

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
