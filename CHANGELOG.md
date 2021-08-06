# Changes

Most recent releases are shown at the top. Each release shows:

- **New**: New classes, methods, functions, etc
- **Changed**: Additional parameters, changes to inputs or outputs, etc
- **Fixed**: Bug fixes that don't change documented behaviour

## 0.0.4 (TBD)

### New:
- initial support for LEAP

### Changed
- Added `backend` parameter to `QuantumAnnealer`

### Fixed:
- N/A


## 0.0.3 (2021-08-05)

### New:
- N/A

### Changed
- removed `local` constructor parameter from `QuantumAnnealer`

### Fixed:
- fixed typo in BraketSampler
- correctly set `local=False` when `device_arn` and `s3_folder` is supplied
- fixed import error in `QuantumAnnealer`


## 0.0.2 (2021-08-02)

### New:
- N/A

### Changed
- Changed default shots for QAOA
- `fit` changed to `execute`

### Fixed:
- N/A

## 0.0.1 (2021-07-30)

### New:
- first release

### Changed
- N/A

### Fixed:
- N/A
