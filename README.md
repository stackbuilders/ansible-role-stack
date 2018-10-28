# Ansible Role: Haskell Stack

Install Haskell Stack on Debian/Ubuntu servers.

## Getting Started

Add the role to your `requirements.yml` file:

```yaml
- src: https://github.com/stackbuilders/ansible-haskell-stack
  name: haskell-stack
```

Install the dependencies:

```
$ ansible-galaxy install -r requirements.yml
```

Add the role to your playbook:

```yaml
- hosts: all
  roles:
    - role: haskell-stack
      become: true
```

## Role Variables

This section list all variables that could be overwritten, along with their
[default values](defaults/main.yml):

### haskell_stack_dependencies

Extra dependencies required by stack binary:

```yaml
haskell_stack_dependencies:
  - g++
  - gcc
  - git
  - gnupg
  - libc6-dev
  - libffi-dev
  - libgmp-dev
  - make
  - xz-utils
  - zlib1g-dev
```

### haskell_stack_version

The stack version to be downloaded:

```yaml
haskell_stack_version: 1.9.1
```

### haskell_stack_bin_dir

The target directory to copy stack binary:

```yaml
haskell_stack_bin_dir: /usr/local/bin
```

## License

Released under the [MIT License](LICENSE).
