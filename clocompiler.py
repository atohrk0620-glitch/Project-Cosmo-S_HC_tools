class GeOpsCore:
    def __init__(self, input_data):
        self.heavy_numbers = self._detect_overlaps(input_data)
        self.annihilation_code = None
        self.persistent_core = None

    def process(self):
        overlapped_regions = self._find_heavy_overlaps()
        self.annihilation_code = self._convert_annihilation_to_code(overlapped_regions)
        self.persistent_core = self._execute_annihilation()
        return self._continuous_max_precision_run()

    def _convert_annihilation_to_code(self, overlaps):
        executable_operations = []
        for overlap in overlaps:
            code_fragment = self._annihilation_to_executable(overlap)
            executable_operations.append(code_fragment)
        return executable_operations

    def _continuous_max_precision_run(self):
        while True:
            yield self._max_precision_operation(self.persistent_core)
