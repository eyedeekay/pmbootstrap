"""
Copyright 2017 Oliver Smith

This file is part of pmbootstrap.

pmbootstrap is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pmbootstrap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pmbootstrap.  If not, see <http://www.gnu.org/licenses/>.
"""
import pmb.chroot
import pmb.chroot.apk_static
import pmb.config
import pmb.helpers.repo
import pmb.helpers.run
import pmb.parse.arch


def qemu_workaround_aarch64(args, suffix="buildroot_aarch64"):
    """
    Qemu has a bug in aarch64 emulation, that causes abuild-tar to omit files
    from the archives it generates in some cases. This workaround copies the
    abuild-tar binary from the native chroot into the buildroot_aarch64 and
    installs a wrapper to use it. That way we bypass emulation and it works as
    expected again.

    https://github.com/postmarketOS/pmbootstrap/issues/546
    """

    # Build and install abuild-aarch64-qemu-workaround
    pkgname = "abuild-aarch64-qemu-workaround"
    pmb.build.package(args, pkgname, "aarch64", True,
                      init_buildenv=False)
    pmb.chroot.apk.install(args, [pkgname], suffix, False)
