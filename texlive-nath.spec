Name:		texlive-nath
Version:	20061222
Release:	1
Summary:	Natural mathematics notation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nath
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nath.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nath/nath.sty
%doc %{_texmfdistdir}/doc/latex/nath/README
%doc %{_texmfdistdir}/doc/latex/nath/nathguide.pdf
%doc %{_texmfdistdir}/doc/latex/nath/nathguide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
