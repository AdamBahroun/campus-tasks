#!/usr/bin/env bash
set -u
errors=0
required=(README.md .gitignore .env.example docs/api.md docs/setup.md)
echo &quot;[CHECK] Campus Tasks&quot;
for file in &quot;${required[@]}&quot;; do
if [[ -f &quot;$file&quot; ]]; then
echo &quot;[OK] $file&quot;
else
echo &quot;[ERREUR] fichier absent: $file&quot; &gt;&amp;2
errors=$((errors + 1))
fi
done
if git ls-files | grep -Eq &#39;(^|/)\.env$&#39;; then
echo &quot;[ERREUR] un fichier .env est suivi par Git&quot; &gt;&amp;2
errors=$((errors + 1))
else
echo &quot;[OK] aucun .env suivi&quot;
fi
if [[ $errors -gt 0 ]]; then
echo &quot;[ECHEC] $errors erreur(s)&quot; &gt;&amp;2
exit 1
fi
echo &quot;[SUCCES] contrôles validés&quot;
exit 0