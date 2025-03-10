name: Bug Report
description: File a bug report.
title: "[Bug]: "
labels: ["bug"]
assignees:
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!
  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Also tell us, what did you expect to happen?
      placeholder: Tell us what you see!
      value: "A bug happened!"
    validations:
      required: true
    - type: dropdown
    id: device
    attributes:
      label: Device Type
      description: What device are you using?
      options:
        - N86P
        - N120P
        - S6
        - T6E
        - Other
      default: 0
    validations:
      required: true
  - type: dropdown
    id: version
    attributes:
      label: Firmware Version
      description: What firmware version are you running on?
    validations:
      required: false
  - type: textarea
    id: version
    attributes:
      label: Version
      description: What version of our software are you running?
      options:
        - latest final
        - latest beta
        - 2.3.x
        - 2.2.x
      default: 0
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Relevant log output
      description: Please copy and paste any relevant log output. This will be automatically formatted into code, so no need for backticks.
      render: shell
