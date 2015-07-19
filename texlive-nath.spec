# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/nath
# catalog-date 2006-12-22 14:37:19 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-nath
Version:	20061222
Release:	10
Summary:	Natural mathematics notation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nath
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nath.doc.tar.xz
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061222-2
+ Revision: 754248
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061222-1
+ Revision: 719101
- texlive-nath
- texlive-nath
- texlive-nath
- texlive-nath

