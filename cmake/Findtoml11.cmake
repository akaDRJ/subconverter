find_path(toml11_INCLUDE_DIR
    NAMES toml.hpp
    PATH_SUFFIXES include
    PATHS ${toml11_ROOT} $ENV{toml11_ROOT}
)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(toml11 DEFAULT_MSG toml11_INCLUDE_DIR)

if(toml11_FOUND)
    set(toml11_INCLUDE_DIRS ${toml11_INCLUDE_DIR})
endif()

mark_as_advanced(toml11_INCLUDE_DIR toml11_INCLUDE_DIRS)
