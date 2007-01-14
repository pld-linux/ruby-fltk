# TODO: optflags
Summary:	Ruby FLTK GUI library
Summary(pl):	Ruby FLTK - biblioteka GUI
Name:		ruby-fltk
Version:	0.9.6
Release:	0.1
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/ruby-fltk/%{name}-%{version}.tar.bz2
# Source0-md5:	b7885cad303c8624bb3f5988ca806f6c
URL:		http://ruby-fltk.sourceforge.net/
BuildRequires:	fltk-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/FLTK is a Ruby binding for the FLTK (Fast Light ToolKit) GUI
library.

%description -l pl
Ruby/FLTK to wi±zanie jêzyka Ruby do biblioteki graficznego interfejsu
u¿ytkownika FLTK (Fast Light ToolKit).

%package examples
Summary:	Ruby FLTK examples
Summary(pl):	Przyk³ady dla Ruby FLTK
Group:		Development/Libraries

%description examples
Ruby FLTK examples.

%description -l pl
Przyk³ady dla Ruby FLTK.

%prep
%setup -q

%build
ruby extconf.rb
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/ruby-fltk-%{version}/{samples,test}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a samples/*  $RPM_BUILD_ROOT%{_examplesdir}/ruby-fltk-%{version}/samples
cp -a test/*  $RPM_BUILD_ROOT%{_examplesdir}/ruby-fltk-%{version}/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Coverage.txt Coverage_Notes.txt README ToDo doc
%{ruby_sitelibdir}/*.rb
%dir %{ruby_sitelibdir}/fltk
%dir %{ruby_sitelibdir}/fltk/canvas
%{ruby_sitelibdir}/fltk/*.rb
%{ruby_sitelibdir}/fltk/canvas/*.rb

%attr(755,root,root) %{ruby_sitearchdir}/*.so

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/ruby-fltk-%{version}
