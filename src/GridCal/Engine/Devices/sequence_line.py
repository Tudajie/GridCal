# This file is part of GridCal.
#
# GridCal is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GridCal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GridCal.  If not, see <http://www.gnu.org/licenses/>.

from GridCal.Engine.Devices.types import BranchType
from GridCal.Engine.Devices.meta_devices import EditableDevice, DeviceType, GCProp


class SequenceLineType(EditableDevice):

    def __init__(self, name='SequenceLine', rating=1,
                 R=0, X=0, G=0, B=0, R0=0, X0=0, G0=0, B0=0, tpe=BranchType.Line):
        """
        Constructor
        :param name: name of the model
        :param rating: Line rating in kA
        :param R: Resistance of positive sequence in Ohm/km
        :param X: Reactance of positive sequence in Ohm/km
        :param G: Conductance of positive sequence in Ohm/km
        :param B: Susceptance of positive sequence in Ohm/km
        :param R0: Resistance of zero sequence in Ohm/km
        :param X0: Reactance of zero sequence in Ohm/km
        :param G0: Conductance of zero sequence in Ohm/km
        :param B0: Susceptance of zero sequence in Ohm/km
        """

        EditableDevice.__init__(self,
                                name=name,
                                active=True,
                                device_type=DeviceType.SequenceLineDevice,
                                editable_headers={'name': GCProp('', str, "Name of the line template"),
                                                  'rating': GCProp('kA', float, "Current rating of the line"),
                                                  'R': GCProp('Ohm/km', float, "Positive-sequence "
                                                              "resistance per km"),
                                                  'X': GCProp('Ohm/km', float, "Positive-sequence "
                                                              "reactance per km"),
                                                  'G': GCProp('S/km', float, "Positive-sequence "
                                                              "shunt conductance per km"),
                                                  'B': GCProp('S/km', float, "Positive-sequence "
                                                              "shunt susceptance per km"),
                                                  'R0': GCProp('Ohm/km', float, "Zero-sequence "
                                                               "resistance per km"),
                                                  'X0': GCProp('Ohm/km', float, "Zero-sequence "
                                                               "reactance per km"),
                                                  'G0': GCProp('S/km', float, "Zero-sequence "
                                                               "shunt conductance per km"),
                                                  'B0': GCProp('S/km', float, "Zero-sequence "
                                                               "shunt susceptance per km")},
                                non_editable_attributes=list(),
                                properties_with_profile={})

        self.tpe = tpe

        self.rating = rating

        # impedances and admittances per unit of length
        self.R = R
        self.X = X
        self.G = G
        self.B = B

        self.R0 = R0
        self.X0 = X0
        self.G0 = G0
        self.B0 = B0

