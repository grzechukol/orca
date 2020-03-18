# Copyright 2020 OpenRCA Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from orca.topology.alerts import extractor, handler
from orca.topology.alerts.falco import extractor as falco_extractor


class AlertHandler(handler.AlertHandler):

    @staticmethod
    def create(graph):
        source_mapper = extractor.SourceMapper('falco')
        return AlertHandler(graph, falco_extractor.AlertExtractor(source_mapper))



