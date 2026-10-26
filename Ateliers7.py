import maya.cmds as cmds

# Get the selected object
obj = cmds.ls(selection=True)

if obj:
    obj = obj[0]

    # Set the animation range
    cmds.playbackOptions(minTime=1, maxTime=100)

    # Frame 1: Starting position
    cmds.currentTime(1)
    cmds.setKeyframe(obj, attribute="translateX", value=0)
    cmds.setKeyframe(obj, attribute="translateY", value=0)
    cmds.setKeyframe(obj, attribute="translateZ", value=0)

    # Frame 25: Move right and up
    cmds.currentTime(25)
    cmds.setKeyframe(obj, attribute="translateX", value=5)
    cmds.setKeyframe(obj, attribute="translateY", value=5)
    cmds.setKeyframe(obj, attribute="translateZ", value=5)

    # Frame 50: Move left and forward
    cmds.currentTime(50)
    cmds.setKeyframe(obj, attribute="translateX", value=10)
    cmds.setKeyframe(obj, attribute="translateY", value=10)
    cmds.setKeyframe(obj, attribute="translateZ", value=10)

    # Frame 75: Move right and down
    cmds.currentTime(75)
    cmds.setKeyframe(obj, attribute="translateX", value=20)
    cmds.setKeyframe(obj, attribute="translateY", value=20)
    cmds.setKeyframe(obj, attribute="translateZ", value=20)

    # Frame 100: Final position
    cmds.currentTime(100)
    cmds.setKeyframe(obj, attribute="translateX", value=50)
    cmds.setKeyframe(obj, attribute="translateY", value=50)
    cmds.setKeyframe(obj, attribute="translateZ", value=50)

    # Return to the first frame
    cmds.currentTime(1)