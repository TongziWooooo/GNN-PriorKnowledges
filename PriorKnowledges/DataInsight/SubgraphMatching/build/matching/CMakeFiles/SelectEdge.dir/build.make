# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build

# Include any dependencies generated for this target.
include matching/CMakeFiles/SelectEdge.dir/depend.make

# Include the progress variables for this target.
include matching/CMakeFiles/SelectEdge.dir/progress.make

# Include the compile flags for this target's objects.
include matching/CMakeFiles/SelectEdge.dir/flags.make

matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o: matching/CMakeFiles/SelectEdge.dir/flags.make
matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o: ../matching/SelectEdge.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o"
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/matching && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o -c /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/matching/SelectEdge.cpp

matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/SelectEdge.dir/SelectEdge.cpp.i"
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/matching && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/matching/SelectEdge.cpp > CMakeFiles/SelectEdge.dir/SelectEdge.cpp.i

matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/SelectEdge.dir/SelectEdge.cpp.s"
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/matching && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/matching/SelectEdge.cpp -o CMakeFiles/SelectEdge.dir/SelectEdge.cpp.s

matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o.requires:

.PHONY : matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o.requires

matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o.provides: matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o.requires
	$(MAKE) -f matching/CMakeFiles/SelectEdge.dir/build.make matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o.provides.build
.PHONY : matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o.provides

matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o.provides.build: matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o


# Object files for target SelectEdge
SelectEdge_OBJECTS = \
"CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o"

# External object files for target SelectEdge
SelectEdge_EXTERNAL_OBJECTS =

matching/SelectEdge: matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o
matching/SelectEdge: matching/CMakeFiles/SelectEdge.dir/build.make
matching/SelectEdge: matching/CMakeFiles/SelectEdge.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable SelectEdge"
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/matching && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/SelectEdge.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
matching/CMakeFiles/SelectEdge.dir/build: matching/SelectEdge

.PHONY : matching/CMakeFiles/SelectEdge.dir/build

matching/CMakeFiles/SelectEdge.dir/requires: matching/CMakeFiles/SelectEdge.dir/SelectEdge.cpp.o.requires

.PHONY : matching/CMakeFiles/SelectEdge.dir/requires

matching/CMakeFiles/SelectEdge.dir/clean:
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/matching && $(CMAKE_COMMAND) -P CMakeFiles/SelectEdge.dir/cmake_clean.cmake
.PHONY : matching/CMakeFiles/SelectEdge.dir/clean

matching/CMakeFiles/SelectEdge.dir/depend:
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/matching /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/matching /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/matching/CMakeFiles/SelectEdge.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : matching/CMakeFiles/SelectEdge.dir/depend

