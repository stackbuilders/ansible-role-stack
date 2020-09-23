# Ansible Role: Stack

Installs [Haskell Stack](https://docs.haskellstack.org/en/stable/README/) on
Linux.

## Requirements

None.

## Role Variables

This section list all variables that could be overwritten, along with their
[default values](defaults/main.yml):

```yaml
stack_version: 2.3.3
```

The Stack version to be installed.

```yaml
stack_install_dir: /usr/local/bin
```

Directory where Stack is going to be copied.

## Dependencies

None.

## Example Playbook

```yaml
- host: servers
  roles:
    - stackbuilders.stack
```

## License

Released under the [MIT License](LICENSE).

## Author Information

This role was created by Stack Builders.
