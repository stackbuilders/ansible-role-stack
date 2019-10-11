# Ansible Role: Haskell Stack

Installs Haskell Stack on Debian/Ubuntu.

## Requirements

None.

## Role Variables

This section list all variables that could be overwritten, along with their
[default values](defaults/main.yml):

### haskell_stack_version

The Stack version to be installed.

```yaml
haskell_stack_version: 1.9.1
```

### haskell_stack_dependencies

Extra dependencies required by Stack.

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

### haskell_stack_bin_dir

Directory where Stack is going to be installed.

```yaml
haskell_stack_bin_dir: /usr/local/bin
```

## Dependencies

None.

## Example Playbook

```yaml
- host: servers
  roles:
    - stackbuilders.haskell-stack
```

## License

Released under the [MIT License](LICENSE).

## Author Information

This role was created by Stack Builders.
