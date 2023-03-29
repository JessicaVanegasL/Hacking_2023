## Bandit Level 29 → Level 30

## Objetivo

There is a git repository at `ssh://bandit29-git@localhost/home/bandit29-git/repo`. The password for the user `bandit29-git` is the same as for the user `bandit29`.

Clone the repository and find the password for the next level.

## Datos de acceso
 
**Servidor**:  bandit.labs.overthewire.org
**Usuario**: bandit29
**Password**: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

## Solución

```
bandit29@bandit:/tmp/b29$ ls
repo
bandit29@bandit:/tmp/b29$ cd repo
bandit29@bandit:/tmp/b29/repo$ ls
README.md
bandit29@bandit:/tmp/b29/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/b29/repo$ git log
commit 0afe3501277395fbfa017480925edee3df6e8bb5 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    fix username

commit c2606dfc0aef7179bf1ccd6cffa9ed19151facb4
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    initial commit of README.md
bandit29@bandit:/tmp/b29/repo$ git checkout c2606dfc0aef7179bf1ccd6cffa9ed19151facb4
Note: switching to 'c2606dfc0aef7179bf1ccd6cffa9ed19151facb4'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at c2606df initial commit of README.md
bandit29@bandit:/tmp/b29/repo$ git branch
* (HEAD detached at c2606df)
  master
bandit29@bandit:/tmp/b29/repo$ git checkout master
Previous HEAD position was c2606df initial commit of README.md
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
bandit29@bandit:/tmp/b29/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/b29/repo$ git checkout dev
Branch 'dev' set up to track remote branch 'dev' from 'origin'.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/b29/repo$ git status
On branch dev
Your branch is up to date with 'origin/dev'.

nothing to commit, working tree clean
bandit29@bandit:/tmp/b29/repo$ git log
commit fbbce0ec6c80acb0fdc00ebb4b5228dd868fd799 (HEAD -> dev, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    add data needed for development

commit 925c929e0527f14c189b3d617d2bcc60f019f567
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    add gif2ascii

commit 0afe3501277395fbfa017480925edee3df6e8bb5 (origin/master, origin/HEAD, master)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    fix username

commit c2606dfc0aef7179bf1ccd6cffa9ed19151facb4
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    initial commit of README.md
(END)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    add data needed for development

commit 925c929e0527f14c189b3d617d2bcc60f019f567
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    add gif2ascii

commit 0afe3501277395fbfa017480925edee3df6e8bb5 (origin/master, origin/HEAD, master)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    fix username

commit c2606dfc0aef7179bf1ccd6cffa9ed19151facb4
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    initial commit of README.md
~
bandit29@bandit:/tmp/b29/repo$ ls
code  README.md
bandit29@bandit:/tmp/b29/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS
- 
bandit29@bandit:/tmp/b29/repo$ 

```

## Notas adicionales

| Comando | Descripción |
|------------|-------------|
|  git clone |  Permite clonar un repositorio   |
| git log| Muestra los logs de los commits |
| git checkout| Muestra las versiones anteriores y permite navegar entre los branch|
|  git branch |  Permite crear,borrar y listar branches   |
|  git status |  Permite clinformación del actual branch    |


## Referencias

[Git](https://gist.github.com/dasdo/9ff71c5c0efa037441b6)