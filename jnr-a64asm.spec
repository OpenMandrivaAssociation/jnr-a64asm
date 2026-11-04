Name:		jnr-a64asm
Version:	1.0.0
Release:	1
Summary:	Pure Java AArch64 assembler
Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/jnr/jnr-a64asm
Source0:	https://github.com/jnr/jnr-a64asm/archive/refs/tags/jnr-a64asm-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python
BuildSystem:	maven

%description
Pure Java assembler for AArch64, used by jnr-ffi.

%prep
%setup -q -n jnr-a64asm-jnr-a64asm-%{version}
# Javadoc is not packaged, and this plugin release does not run on the current JDK.
python - <<'PY'
import re
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
text = re.sub(
	r"\s*<plugin>\s*<groupId>org\.apache\.maven\.plugins</groupId>\s*<artifactId>maven-javadoc-plugin</artifactId>.*?</plugin>",
	"",
	text,
	count=1,
	flags=re.S,
)
path.write_text(text)
PY

%files -f .mfiles
%doc LICENSE README.md
