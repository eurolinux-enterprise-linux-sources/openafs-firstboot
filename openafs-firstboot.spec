%define __check_files  %{nil}
%define afsvers 1.6

Summary: OpenAFS firstboot scripts
Name: openafs-firstboot
Version: %{afsvers}
Release: 1.sl6
License: GPL 
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Packager: Connie Sieh <csieh@fnal.gov>, Troy Dawson <dawson@fnal.gov> 
Group: Networking/Filesystems
BuildArchitectures: noarch

Source0: openafs-firstboot
Source1: openafs-ThisCell.ANL
Source2: openafs-ThisCell.ATLAS
Source3: openafs-ThisCell.CERN
Source4: openafs-ThisCell.DESY
Source5: openafs-ThisCell.FNAL
Source6: openafs-ThisCell.PSI
Source7: openafs-firstboot.png

%description
This package enables firstboot to configure openafs ThisCell

%prep

%build

###
### install
###
%install
[ $RPM_BUILD_ROOT != / ] && rm -rf $RPM_BUILD_ROOT

# Build install tree
mkdir -p $RPM_BUILD_ROOT/usr/vice/etc
mkdir -p $RPM_BUILD_ROOT/usr/share/firstboot/modules
mkdir -p $RPM_BUILD_ROOT/usr/share/firstboot/pixmaps

# Populate /usr/vice/etc
uve=$RPM_BUILD_ROOT/usr/vice/etc
install -p -m 644 $RPM_SOURCE_DIR/openafs-ThisCell.ANL $uve/ThisCell.ANL
install -p -m 644 $RPM_SOURCE_DIR/openafs-ThisCell.ATLAS $uve/ThisCell.ATLAS
install -p -m 644 $RPM_SOURCE_DIR/openafs-ThisCell.CERN $uve/ThisCell.CERN
install -p -m 644 $RPM_SOURCE_DIR/openafs-ThisCell.DESY $uve/ThisCell.DESY
install -p -m 644 $RPM_SOURCE_DIR/openafs-ThisCell.FNAL $uve/ThisCell.FNAL
install -p -m 644 $RPM_SOURCE_DIR/openafs-ThisCell.PSI $uve/ThisCell.PSI

# Get Firstboot Stuff in there
install -p -m 755 $RPM_SOURCE_DIR/openafs-firstboot $RPM_BUILD_ROOT/usr/share/firstboot/modules/openafs.py
install -p -m 755 $RPM_SOURCE_DIR/openafs-firstboot.png $RPM_BUILD_ROOT/usr/share/firstboot/pixmaps/openafs.png

###
### clean
###
%clean
[ "$RPM_BUILD_ROOT" != "/" -a "x%{debugspec}" != "x1" ] && \
	rm -fr $RPM_BUILD_ROOT

###
### file lists
###
%files
/usr/vice/etc/ThisCell.ANL
/usr/vice/etc/ThisCell.ATLAS
/usr/vice/etc/ThisCell.CERN
/usr/vice/etc/ThisCell.DESY
/usr/vice/etc/ThisCell.FNAL
/usr/share/firstboot/modules/openafs.py
/usr/share/firstboot/pixmaps/openafs.png

%changelog
* Thu Feb 10 2011 Troy Dawson <dawson@fnal.gov> - 1.6-1.SL
- Changed the script to work with SL6

* Mon Apr 02 2007 Troy Dawson <dawson@fnal.gov> - 1.4-1.SL
- Change copyright to license
- Added ThisCell.PSI

* Thu Jun 24 2004 Troy Dawson <dawson@fnal.gov> - 5.SL
- Fixed startup bug for real this time.
- Added check for cell
- Added check so user can say if they want it to start on boot or not

* Tue Jun 15 2004 Troy Dawson <dawson@fnal.gov> - 4.SL
- Fixed error when starting afs from firstboot
- Made package noarch


