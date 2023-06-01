Name:           json-cwx
Version:        0.12
Release:        2%{?commit:.git%{shortcommit}}%{?dist}
Summary:        Modified version of the JSON-C library with extensions

License:        GPL
URL:            https://github.com/LLNL/json-cwx/releases
Source0:        https://github.com/LLNL/%{name}/archive/%{version}.tar.gz

BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake

%description
This is a modified version of the JSON-C library.

Its moniker is json-cwx (json-c with extensions)

The initial version was obtained from here,
https://github.com/json-c/json-c/releases,
numbered 0.12-20140410.

Among other things, it has been modified to support
     * Optimized, homogenously typed, multi-dimensional arrays.
       That is, arrays whose members are NOT json objects but
       the individual array elements in a larger buffer. These
       are 'extarr' object types.
     * Enumerated types.
     * Path-oriented object get/set methods.
     * Path get methods that can accept paths such as "a/gorfo/5/foo/7"
       where if gorfo and foo are array objects, then 5 and 7 are
       treated as array indices. If gorfo and foo are 'normal' objects,
       then '5' and '7' are treated as the member keys of the objects.
     * A find method that is a lot like Unix' find except that it can
       find a matching sub-path from the specified root.

These modifications have not been pushed back to JSON-C implementors.
This is primarily because many of these enhancements kinda sorta fall
outside the original design scope (IMHO) of JSON in general and JSON-C
in particular. In fact, the extarr and enum types break the JSON-C
ascii string syntax.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
sh autogen.sh
%configure
%{make_build}

%install
%{make_install}
cp $RPM_BUILD_DIR/%{name}-%{version}/LICENSE .
rm -f %{buildroot}%{_libdir}/libjson-cwx.a

%files
%license LICENSE
%{_includedir}/*
%{_libdir}/*

%changelog
* Tue Jul 04 2023 Brian J. Murrell <brian.murrell@intel.com> - 0.12-2
- Don't install static lib

* Tue Jun 16 2020 Phil Henderson <phillip.henderson@intel.com> - 0.12-1
- Initial version
