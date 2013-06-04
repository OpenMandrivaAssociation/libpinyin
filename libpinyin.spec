%define major 4
%define beta %{nil}
%define scmrev %{nil}
%define libname %mklibname pinyin %{major}
%define devname %mklibname pinyin -d
%define staticname %mklibname pinyin -d -s

Name: libpinyin
Version: 0.9.91
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 1
Source: http://ufpr.dl.sourceforge.net/project/libpinyin/libpinyin/libpinyin-%version.tar.gz
%else
Release: 0.%{scmrev}.1
Source: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.%{scmrev}.1
Source: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: PinYin input library
URL: http://libpinyin.sf.net/
License: GPL
Group: System/Libraries

%description
PinYin input library

%package -n %{libname}
Summary: PinYin input library
Group: System/Libraries

%description -n %{libname}
PinYin input library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{staticname}
Summary: Static libraries for linking to %{name}
Group: Development/C
Requires: %{devname} = %{EVRD}

%description -n %{staticname}
Static libraries for linking to %{name}.

Install this package if you wish to develop or compile applications using
%{name} statically (users of the resulting binary won't
need %{name} installed
with static linking).

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%_libdir/libpinyin
%_mandir/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n %{staticname}
%{_libdir}/*.a
