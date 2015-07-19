%define major	5
%define libname %mklibname pinyin %{major}
%define devname %mklibname pinyin -d

Summary:	PinYin input library
Name:		libpinyin
Version:	1.1.0
Release:	2
License:	GPLv2
Group:		System/Libraries
Url:		http://libpinyin.sf.net/
Source0:	http://ufpr.dl.sourceforge.net/project/libpinyin/libpinyin/libpinyin-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	db6-devel
BuildRequires:	pkgconfig(glib-2.0)

%description
PinYin input library

%package -n %{libname}
Summary:	PinYin input library
Group:		System/Libraries

%description -n %{libname}
PinYin input library

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q

%build
autoreconf -fiv
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_libdir}/libpinyin
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libpinyin.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

