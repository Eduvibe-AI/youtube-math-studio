import os
import cv2

jobs = [
    {
        "video": "lecture_video21.mp4",
        "dir": "captures_v21",
        "frames": [
            ("01_intro_ratio_concept.jpg", 25.0),
            ("02_cubic_vs_trig_ratio.jpg", 110.0),
            ("03_eight_box_division.jpg", 240.0),
            ("04_ratio_special_angles.jpg", 390.0),
            ("05_half_height_one_third.jpg", 540.0),
            ("06_symmetry_inflection_tangent.jpg", 690.0),
            ("07_exam_speed_solving.jpg", 840.0),
            ("08_csat_killer_application.jpg", 990.0),
            ("09_final_ratio_formula.jpg", 1150.0),
        ]
    },
    {
        "video": "lecture_video22.mp4",
        "dir": "captures_v22",
        "frames": [
            ("01_n_axis_intro.jpg", 60.0),
            ("02_inner_outer_composition.jpg", 300.0),
            ("03_n_axis_rotation_setup.jpg", 600.0),
            ("04_turning_points_extrema.jpg", 960.0),
            ("05_piecewise_linear_n_axis.jpg", 1320.0),
            ("06_quadratic_inside_linear.jpg", 1680.0),
            ("07_periodic_function_composition.jpg", 2100.0),
            ("08_root_count_determination.jpg", 2520.0),
            ("09_daechi_secret_technique.jpg", 2940.0),
            ("10_master_summary_chart.jpg", 3250.0),
        ]
    },
    {
        "video": "lecture_video23.mp4",
        "dir": "captures_v23",
        "frames": [
            ("01_parabola_seven_properties.jpg", 60.0),
            ("02_focal_chord_harmonic_mean.jpg", 240.0),
            ("03_directrix_orthogonal_tangents.jpg", 480.0),
            ("04_tangent_projection_isosceles.jpg", 720.0),
            ("05_optical_reflection_property.jpg", 960.0),
            ("06_subtangent_axis_symmetry.jpg", 1200.0),
            ("07_focal_radius_circle_tangent.jpg", 1440.0),
            ("08_archimedes_area_ratio.jpg", 1680.0),
            ("09_exam_focal_problems.jpg", 1920.0),
            ("10_seven_formula_recap.jpg", 2050.0),
        ]
    }
]

for job in jobs:
    vpath = job["video"]
    out_dir = job["dir"]
    os.makedirs(out_dir, exist_ok=True)
    if not os.path.exists(vpath):
        print(f"Skipping {vpath}, file not yet found.")
        continue
    
    cap = cv2.VideoCapture(vpath)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"[{vpath}] FPS: {fps:.2f}, Frames: {total_frames}, Dur: {total_frames/fps:.1f}s")

    for name, sec in job["frames"]:
        frame_idx = min(int(sec * fps), total_frames - 1)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(out_dir, name), frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
            print(f"  Saved {name} at {sec}s")
        else:
            print(f"  FAILED to read {name} at {sec}s")
    cap.release()

print("Extraction script done!")
