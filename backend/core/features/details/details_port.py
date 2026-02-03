#
#   Imports
#

import uuid

from abc import ABC, abstractmethod

# Perso

from core.shared.enums.details_tab_type import DetailsTabType
from core.features.details.details import DetailsTab


#
#   Ports
#

class DetailsDBPort(ABC):

    @abstractmethod
    async def get_detailed_tab(
        self,
        year: int,
        trans_type: str,
        user_id: uuid.UUID,
        tab_type: DetailsTabType
    ) -> DetailsTab:
        """
            Gets the table that pending on the tab_typ (table type)
            sums up the amount spent per category per month.
            Its a table with a header row that are the month, the
            header column with the name of the categories. The categories
            are sorted alphabetically and displays the category with levels
            0 first but each time there are childs to a category then the
            sum up amount of the childs are displayed. Finally, there are
            a total row and column at the end.
        """
        pass
