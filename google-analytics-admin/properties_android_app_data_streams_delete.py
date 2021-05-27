#!/usr/bin/env python

# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Analytics Admin API sample application which deletes the Android app
data stream.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/properties.androidAppDataStreams/delete
for more information.
"""
# [START analyticsadmin_properties_android_app_data_streams_delete]
from google.analytics.admin import AnalyticsAdminServiceClient


def run_sample():
    """Runs the sample."""

    # !!! ATTENTION !!!
    #  Running this sample may change/delete your Google Analytics account
    #  configuration. Make sure to not use the Google Analytics property ID from
    #  your production environment below.

    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID (e.g. "123456") before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"

    # TODO(developer): Replace this variable with your Android app data stream ID
    #  (e.g. "123456") before running the sample.
    stream_id = "YOUR-ANDROID-APP-DATA-STREAM-ID"

    delete_android_app_data_stream(property_id, stream_id)


def delete_android_app_data_stream(property_id, stream_id):
    """Deletes the Android app data stream."""
    client = AnalyticsAdminServiceClient()
    client.delete_android_app_data_stream(
        name=f"properties/{property_id}/androidAppDataStreams/{stream_id}"
    )
    print("Android app data stream deleted")


# [END analyticsadmin_properties_android_app_data_streams_delete]


if __name__ == "__main__":
    run_sample()
