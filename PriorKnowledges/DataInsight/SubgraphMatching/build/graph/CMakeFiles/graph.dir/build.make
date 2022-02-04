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
include graph/CMakeFiles/graph.dir/depend.make

# Include the progress variables for this target.
include graph/CMakeFiles/graph.dir/progress.make

# Include the compile flags for this target's objects.
include graph/CMakeFiles/graph.dir/flags.make

graph/CMakeFiles/graph.dir/graph.cpp.o: graph/CMakeFiles/graph.dir/flags.make
graph/CMakeFiles/graph.dir/graph.cpp.o: ../graph/graph.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object graph/CMakeFiles/graph.dir/graph.cpp.o"
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/graph && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/graph.dir/graph.cpp.o -c /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/graph/graph.cpp

graph/CMakeFiles/graph.dir/graph.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/graph.dir/graph.cpp.i"
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/graph && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/graph/graph.cpp > CMakeFiles/graph.dir/graph.cpp.i

graph/CMakeFiles/graph.dir/graph.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/graph.dir/graph.cpp.s"
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/graph && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/graph/graph.cpp -o CMakeFiles/graph.dir/graph.cpp.s

graph/CMakeFiles/graph.dir/graph.cpp.o.requires:

.PHONY : graph/CMakeFiles/graph.dir/graph.cpp.o.requires

graph/CMakeFiles/graph.dir/graph.cpp.o.provides: graph/CMakeFiles/graph.dir/graph.cpp.o.requires
	$(MAKE) -f graph/CMakeFiles/graph.dir/build.make graph/CMakeFiles/graph.dir/graph.cpp.o.provides.build
.PHONY : graph/CMakeFiles/graph.dir/graph.cpp.o.provides

graph/CMakeFiles/graph.dir/graph.cpp.o.provides.build: graph/CMakeFiles/graph.dir/graph.cpp.o


# Object files for target graph
graph_OBJECTS = \
"CMakeFiles/graph.dir/graph.cpp.o"

# External object files for target graph
graph_EXTERNAL_OBJECTS =

graph/libgraph.so: graph/CMakeFiles/graph.dir/graph.cpp.o
graph/libgraph.so: graph/CMakeFiles/graph.dir/build.make
graph/libgraph.so: graph/CMakeFiles/graph.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libgraph.so"
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/graph && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/graph.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
graph/CMakeFiles/graph.dir/build: graph/libgraph.so

.PHONY : graph/CMakeFiles/graph.dir/build

graph/CMakeFiles/graph.dir/requires: graph/CMakeFiles/graph.dir/graph.cpp.o.requires

.PHONY : graph/CMakeFiles/graph.dir/requires

graph/CMakeFiles/graph.dir/clean:
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/graph && $(CMAKE_COMMAND) -P CMakeFiles/graph.dir/cmake_clean.cmake
.PHONY : graph/CMakeFiles/graph.dir/clean

graph/CMakeFiles/graph.dir/depend:
	cd /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/graph /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/graph /home/tongzi/Capstone/PriorKnowledges/DataInsight/SubgraphMatching/build/graph/CMakeFiles/graph.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : graph/CMakeFiles/graph.dir/depend

