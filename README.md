Node ros2 pour controler les pamis à partir d'un page web.

En plus de cela, une interface graphique pour controler les pamis avec le PC.

Aller dans le workspace ros2 puis : 

```
git clone https://gitlab-research.centralesupelec.fr/club-tech/ctrl_pamis_web_ros/
```
```
colcon build --packages-select ctrl_pamis_web_ros
```
```
source install/setup.bash
```
```
ros2 run ctrl_pamis_web_ros ctrl_pamis_web 
```
