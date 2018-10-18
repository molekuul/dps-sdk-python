import logging
import time

from dvlssdk.InitHelpers import *

dvlsLogger = logging.getLogger('dvlssdk')


def sanitize_options(entry, options):
    for k, v in options.items():
        function_name = k
        try:
            success = globals()[function_name](k, v, options)
            if not success:
                return success
        except KeyError:
            options[k]

    if 'RoleOverride' not in options:
        SetDefaultRoleOverride(entry, options)


def PasswordTemplateId(key, value, options):
    if value == 'Inherited' or value == 'None':
        options[key] = "<<" + value + ">>"
    else:
        options[key] = value


def MinimumLengthCount(key, value, options):
    options['PasswordTemplateId'] = "<<Custom>>"


def MinimumLowerCaseCount(key, value, options):
    options['PasswordTemplateId'] = "<<Custom>>"


def MinimumNumericCount(key, value, options):
    options['PasswordTemplateId'] = "<<Custom>>"


def MinimumSymbolCount(key, value, options):
    options['PasswordTemplateId'] = "<<Custom>>"


def MnimumUpperCaseCount(key, value, options):
    options['PasswordTemplateId'] = "<<Custom>>"


def TimeBasedUsageTimePeriod(key, value, options):
    if isinstance(value, str):
        usage_hours = value.split('-')
        if is_hh_mm_time(usage_hours[0]) and is_hh_mm_time(usage_hours[1]):
            options['TimeBasedUsageHours'] = 'Custom'
            options['TimeBasedUsageStartTime'] = usage_hours[0]
            options['TimeBasedUsageEndTime'] = usage_hours[1]


def TimeBasedUsageDays(key, value, options):
        if isinstance(value, str):
            days = init_enum('generated', 'Days')
            selected_day_of_week = 0
            usage_days = value.split('-')
            for usageDay in usage_days:
                if usageDay in days.__members__:
                    selected_day_of_week += days.value_from_name(usageDay)
            options[key] = 'Custom'
            options['SelectedDayOfWeek'] = selected_day_of_week


def RoleOverride(key, value, options):
    if value == 'Default' or value == 'Never' or value == 'Everyone':
        conflict = False
        if 'ViewRoles' in options:
            conflict = True
        else:
            for item in options['SecurityRoleRight'].__members__.items():
                if item in options:
                    conflict = True
        if conflict:
            dvlsLogger.error("RoleOverride must be omitted in order to use custom values.  Aborting entry creation")
    else:
        dvlsLogger.error("Incorrect value '" + value + "' for RoleOverride")


def SetDefaultRoleOverride(entry, options):
    if 'RoleOverride' in options:
        security_role_right = options['RoleOverride']
        set_role_override = False
        if 'ViewRoles' in options:
            entry.Security.ViewOverride = 1
            set_role_override = True
        for item, value in security_role_right.__members__.items():
            if item in options:
                set_role_override = True
                options['Right'] = item
                if isinstance(options[item], list):
                    options['RoleValues'] = str(
                        options[item])[1:-1]
                    options['Override'] = 'Custom'
                else:
                    options['RoleValues'] = ''
                    options['Override'] = options[item]
                connection_permission = init_model('generated', 'ConnectionPermission')
                entry.Security.Permissions.append(fill_data(connection_permission, options))
        if set_role_override:
            entry.Security.RoleOverride = 1


def is_hh_mm_time(time_string):
    try:
        time.strptime(time_string, '%H:%M')
    except ValueError:
        return False
    return len(time_string) == 5