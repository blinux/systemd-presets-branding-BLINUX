#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:           systemd-presets-branding-BLINUX
Version:        2.0
Release:        2
Summary:        Provides systemd-presets branding
Group:		System/Base
License:        BSD-2-Clause

BuildArch:      noarch
Source0:        90-default-BLINUX.preset
Source1:        99-default-disable.preset
BuildRequires:  systemd
Requires:	systemd
Provides:       systemd-presets-branding = %{version}
Supplements:    packageand(systemd:branding-BLINUX)
Conflicts:      otherproviders(systemd-presets-branding)
%systemd_requires

Url:            https://www.blinux.fr
Packager:       Emmanuel Vadot <elbarto@bocal.org>
Vendor:		Blinux

%description
BLINUX branding base package

%prep

%build

%install
mkdir -p %{buildroot}/usr/lib/systemd/system-preset
install -m 644 %{SOURCE0}  %{buildroot}/usr/lib/systemd/system-preset/
install -m 644 %{SOURCE1}  %{buildroot}/usr/lib/systemd/system-preset/

%post
systemctl daemon-reload >/dev/null 2>&1 || :

%postun
if [ $1 -eq 0 ]; then
systemctl daemon-reload >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root)
/usr/lib/systemd/system-preset/*

%changelog
* Tue Aug 12 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0
- Package creation
