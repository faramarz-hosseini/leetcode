class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        placed_boxes = 0
        total_units = 0

        for boxinfo in boxTypes:
            for box in range(1, boxinfo[0] + 1):
                if placed_boxes == truckSize:
                    return total_units
                placed_boxes += 1
                total_units += boxinfo[1]

        return total_units
